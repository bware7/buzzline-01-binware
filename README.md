# Buzzline-01-Bin Ware

This project demonstrates streaming data using Python generators and real-time log monitoring. It includes a custom producer that generates social media post messages (e.g., "I just posted a photo! It was awesome.") and a consumer that monitors the log file in real-time, alerting when a message contains the word "awesome".

## Project Overview

This streaming analytics project showcases:
- **Python Generators**: Efficient memory usage with yield statements
- **Real-time Data Streaming**: Continuous message generation and consumption
- **Pattern Detection**: Alerting system for specific keywords
- **Concurrent Processing**: Running producer and consumer simultaneously

## Setup

Follow the setup instructions in [pro-analytics-01, Part 1](https://github.com/denisecase/pro-analytics-01) to configure your machine with Python 3.11 and required tools. Then, initialize the project as described in [pro-analytics-01, Part 2](https://github.com/denisecase/pro-analytics-01).

### Prerequisites
- Python 3.11 or higher
- Virtual environment (`.venv`)
- Required packages from `requirements.txt`

## Custom Producer: `basic_producer_binware.py`

The producer generates randomized social media post messages combining:
- **Actions**: posted, shared, liked, commented on, retweeted
- **Topics**: a photo, a video, a blog, a quote, a thread
- **Adjectives**: awesome, hilarious, inspiring, creative, epic

Messages are generated every 3 seconds (configurable via `.env` file) and logged to `logs/project_log.log`.

### Running the Producer (Terminal 1)

#### Windows
```bash
.venv\Scripts\activate
py -m producers.basic_producer_binware
```

#### Mac/Linux
```bash
source .venv/bin/activate
python3 -m producers.basic_producer_binware
```

### Sample Producer Output
```
📱 I just posted a video! It was creative.
📱 I just shared a blog! It was awesome.
📱 I just liked a quote! It was inspiring.
```

## Custom Consumer: `basic_consumer_binware.py`

The consumer:
- Monitors the log file in real-time
- Displays each consumed social media message
- Alerts when detecting messages containing "awesome"
- Logs warnings for awesome messages

### Running the Consumer (Terminal 2)

#### Windows
```bash
.venv\Scripts\activate
py -m consumers.basic_consumer_binware
```

#### Mac/Linux
```bash
source .venv/bin/activate
python3 -m consumers.basic_consumer_binware
```

### Sample Consumer Output
```
Consumer is ready and monitoring for social media log messages...
------------------------------------------------------------
📱 Consumed: I just posted a video! It was creative.
📱 Consumed: I just shared a blog! It was awesome.
============================================================
🚨 ALERT: An awesome social media message detected!
📍 Message: I just shared a blog! It was awesome.
============================================================
📱 Consumed: I just liked a quote! It was inspiring.
```

## How It Works

1. **Start the Producer**: Run the producer script in Terminal 1. It will begin generating social media messages every 3 seconds.

2. **Start the Consumer**: Run the consumer script in Terminal 2. It will start monitoring the log file and display messages in real-time.

3. **Watch the Magic**: As the producer creates messages, the consumer reads them instantly. When an "awesome" message appears, you'll see a special alert!

4. **Stop the Processes**: Press `CTRL+C` (or `CMD+C` on Mac) in each terminal to stop the scripts.

## Project Structure

```
buzzline-01-binware/
├── producers/
│   └── basic_producer_binware.py    # Custom social media message generator
├── consumers/
│   └── basic_consumer_binware.py    # Real-time log monitor with alerts
├── logs/
│   └── project_log.log              # Generated log file
├── utils/
│   └── utils_logger.py              # Logging utilities
├── .env                             # Configuration (MESSAGE_INTERVAL_SECONDS)
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## Key Features

- **Memory Efficient**: Uses Python generators to yield messages one at a time
- **Real-time Processing**: Consumer reads new log entries as they're written
- **Pattern Detection**: Automatically identifies and alerts on "awesome" messages
- **Concurrent Execution**: Producer and consumer run independently in separate terminals
- **Configurable**: Message interval can be adjusted via `.env` file

## Customizations Made

### Producer Enhancements
- Created social media-themed message generator
- Implemented random selection from predefined word lists
- Added variety with 5 actions × 5 topics × 5 adjectives = 125 possible messages

### Consumer Enhancements
- Real-time log file monitoring with position tracking
- Visual message consumption with emoji indicators
- Alert system with highlighted notifications for "awesome" messages
- Warning-level logging for detected patterns

## Troubleshooting

- **Consumer not showing messages**: Ensure the producer is running first
- **Log file not found**: Check that the `logs` directory exists
- **Import errors**: Activate the virtual environment before running scripts
- **No alerts showing**: Wait for a message containing "awesome" (appears randomly)

## Author

Created by Bin Ware for the Streaming Data Analytics course at Northwest Missouri State University.