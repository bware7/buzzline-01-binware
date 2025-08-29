"""
Generate social media post messages every few seconds.
"""

#####################################
# Import Modules
#####################################

import os
import random
import time
from dotenv import load_dotenv
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

load_dotenv()

#####################################
# Define Getter Functions for .env Variables
#####################################

def get_message_interval() -> int:
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", "3")
    interval: int = int(return_value)
    logger.info(f"Messages will be sent every {interval} seconds.")
    return interval

#####################################
# Define global variables
#####################################

# Define lists for generating social media post messages
ADJECTIVES: list = ["awesome", "hilarious", "inspiring", "creative", "epic"]
ACTIONS: list = ["posted", "shared", "liked", "commented on", "retweeted"]
TOPICS: list = ["a photo", "a video", "a blog", "a quote", "a thread"]

#####################################
# Define a function to generate social media messages
#####################################

def generate_messages():
    """
    Generate a stream of social media post messages.
    Yields one message at a time for memory efficiency.
    Runs continuously until interrupted (CTRL+C).
    """
    while True:
        adjective = random.choice(ADJECTIVES)
        action = random.choice(ACTIONS)
        topic = random.choice(TOPICS)
        yield f"I just {action} {topic}! It was {adjective}."

#####################################
# Define main() function to run this producer
#####################################

def main() -> None:
    """
    Main entry point for the social media post producer.
    """
    logger.info("START social media post producer...")
    logger.info("Hit CTRL c (or CMD c) to close.")
    
    interval_secs: int = get_message_interval()

    try:
        for message in generate_messages():
            logger.info(message)
            time.sleep(interval_secs)
    except KeyboardInterrupt:
        logger.info("Producer stopped by user.")

    logger.info("NOTE: See the `logs` folder to learn more.")
    logger.info("END producer.....")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()