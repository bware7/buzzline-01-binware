"""
Read a log file in real-time and alert on social media messages containing 'awesome'.
"""

#####################################
# Import Modules
#####################################

import time
from utils.utils_logger import logger, get_log_file_path

#####################################
# Define message processing function
#####################################

def process_message(log_file: str) -> None:
    """
    Read a log file and process each social media message from the producer.
    Alerts when a producer message contains 'awesome'.

    Args:
        log_file (str): The path to the log file to read.
    """
    print("Consumer is ready and monitoring for social media log messages...")
    print("-" * 60)
    
    # Track the last position we read from
    last_position = 0
    
    while True:
        try:
            with open(log_file, "r") as file:
                # Move to the last position we read from
                file.seek(last_position)
                
                # Read new lines
                new_lines = file.readlines()
                
                # Update our position
                last_position = file.tell()
                
                # Process each new line
                for line in new_lines:
                    # Check if this line contains a social media message from the producer
                    if "I just" in line and "__main__:main" in line:
                        # Extract the message part after the last " - "
                        if " - " in line:
                            social_msg = line.split(" - ")[-1].strip()
                            print(f"📱 Consumed: {social_msg}")
                            
                            # Check for "awesome" in the message
                            if "awesome" in social_msg.lower():
                                print("=" * 60)
                                print("🚨 ALERT: An awesome social media message detected!")
                                print(f"📍 Message: {social_msg}")
                                print("=" * 60)
                                logger.warning(f"ALERT: Awesome message detected - {social_msg}")
                
        except FileNotFoundError:
            print(f"Waiting for log file to be created at: {log_file}")
            last_position = 0
        except Exception as e:
            print(f"Error reading file: {e}")
        
        # Wait a bit before checking for new messages
        time.sleep(0.5)

#####################################
# Define main() function to run this consumer
#####################################

def main() -> None:
    """
    Main entry point for the social media consumer.
    """
    logger.info("START social media consumer...")
    logger.info("Hit CTRL c (or CMD c) to close.")
    
    log_file_path = get_log_file_path()
    logger.info(f"Reading file located at {log_file_path}")

    try:
        process_message(log_file_path)
    except KeyboardInterrupt:
        print("\nConsumer stopped by user.")
        logger.info("Consumer stopped by user.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    
    logger.info("END social media consumer.....")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()