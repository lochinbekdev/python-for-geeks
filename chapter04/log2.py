import logging

logger1=logging.getLogger("jdpuPF")
logging.basicConfig()
logger1.setLevel(logging.INFO)
logger1.warning("This is a warning message")
logger1.info("This is a info message")
logger1.debug("This is a debug logger")
logging.info("This is a info  message")


