import logging
import azure.functions as func

app = func.FunctionApp()

@app.schedule(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger_vscode(myTimer: func.TimerRequest) -> None:
    logging.info('---[START]---')
    logging.info('!!!!! Hello, world !!!!!')

    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')
    logging.info('---[END]---')