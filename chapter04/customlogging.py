import logging

logger = logging.getLogger("JdpuPF")
jdpuPF_handler = logging.StreamHandler()
jdpuPF_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
jdpuPF_handler.setFormatter(jdpuPF_formatter)
logger.addHandler(jdpuPF_handler)
logger.setLevel(logging.INFO)
logger.warning("This is a warning message")
logger.info("This is a info message")
logger.debug("This is a debug message")
