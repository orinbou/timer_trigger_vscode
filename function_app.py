import logging
import time
import azure.functions as func

app = func.FunctionApp()

@app.schedule(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger_vscode(myTimer: func.TimerRequest) -> None:
    logging.info('---[START]---')
    time.sleep(0.1)
    logging.info('!!!!! Hello, world !!!!!')
    time.sleep(0.1)

    if myTimer.past_due:
        logging.info('The timer is past due!')
        time.sleep(0.1)

    logging.info('Python timer trigger function executed.')
    time.sleep(0.1)
    logging.info('---[END]---')