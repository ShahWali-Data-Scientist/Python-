import logging
logging.basicConfig(filename="test.log",level= logging.INFO)
logging.info("This is my first code for logging")
l = [1,2,3,4,5,6,7,7]
for i in l :
    if i == 2 :
        logging.info(l)