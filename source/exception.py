import sys
import logging

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=erro_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script[{0}] line number[{1}] error message[{2}]".format(file_name,exc_tb.lineno,str(error))

    return error_message




    class CustomException(Exception):
        def __init__(self,error_message,error_detail:sys):
            super.__init__(error_message)
            self.error_message = error_message_details(error_message,error_detail=error_detail)


        def __str__(self):
            return self.error_message
            
if __name__=="__main__":

    try:
        a=1/10
    except:
        logging.info("Divide by zero error")
        raise CustomException


