import sys

def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    line_number = exc_tb.tb_lineno
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_mass = str(error)
    
    error_message = f"Error occoured in file name:->[{file_name}] at line number:->[{line_number}] error message is:->[{error_mass}]."
    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error=error_message,error_detail=error_details)
        
    def __str__(self):
        return self.error_message