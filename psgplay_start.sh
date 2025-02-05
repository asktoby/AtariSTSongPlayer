#!/bin/bash

# Start pigpiod daemon if it's not running
if ! pgrep -x "pigpiod" > /dev/null; then
    echo "Starting pigpiod daemon..."
    sudo pigpiod
fi

# Set GPIO 26 as input with pull-up resistor enabled
GPIO_PIN=26
echo "Setting GPIO pin $GPIO_PIN as input with pull-up resistor..."
pigs p $GPIO_PIN 1

# Function to stop psgplay process safely
stop_psgplay() {
    if [[ -n "$PSG_PID" ]]; then
        echo "Stopping psgplay process with PID: $PSG_PID..."
        kill -TERM "$PSG_PID" 2>/dev/null

        # Wait for process to fully exit
        for i in {1..10}; do
            if ! ps -p "$PSG_PID" > /dev/null; then
                echo "psgplay stopped."
                break
            fi
            sleep 0.1
        done
    fi
}

# Cleanup function to ensure proper termination
cleanup() {
    echo "Cleaning up and stopping psgplay..."
    stop_psgplay
    exit 0
}

# Trap signals for cleanup
trap cleanup SIGINT SIGTERM

while true; do
    # Find a random .sndh file
    FILE=$(find /home/pi/music -type f -name "*.sndh" | shuf -n 1)
    echo "Selected file: $FILE"

# Get the number of tracks
TRACKS=$(./psgplay/psgplay "$FILE" -i | grep "##" | awk '{print $4}')

# If TRACKS is empty or not a number, set it to 1
if ! [[ "$TRACKS" =~ ^[0-9]+$ ]]; then
    TRACKS=1
fi
echo "Number of tracks: $TRACKS"

    # Pick a random track
    TRACK_TO_PLAY=$((RANDOM % TRACKS + 1))
    echo "Selected track: $TRACK_TO_PLAY"

    # Play the selected track in the background
    ./psgplay/psgplay "$FILE" -t "$TRACK_TO_PLAY" &
    PSG_PID=$!
    echo "psgplay started with PID: $PSG_PID"

    # Wait for GPIO switch press
    while true; do
        GPIO_STATE=$(pigs r $GPIO_PIN)

if [[ $GPIO_STATE -eq 0 ]]; then
        echo "GPIO state: 0"
        stop_psgplay
        break
    fi


        if [[ "$GPIO_STATE" -eq 0 ]]; then
            stop_psgplay
            break
        fi
        sleep 0.1
    done

    # Debounce: wait for switch to be released
    while [[ $(pigs r $GPIO_PIN) -eq 0 ]]; do
        sleep 0.1
    done

    # Ensure psgplay is fully stopped before next loop
    stop_psgplay

    # Avoid rapid looping
    sleep 1
done
