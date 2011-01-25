from subprocess import PIPE, Popen
import logging


def call(cmd, dryrun=False):
    logging.debug( 'calling:' )
    logging.debug( cmd )
    if not dryrun:
        x= Popen(cmd, stdout=PIPE,stderr=PIPE, shell=1).communicate()
        def format_output(s):
            s=s.replace('\x08',' ') # for unrar in eclipse
            return s
        logging.debug( 'stdout output:\n' + format_output(x[0]) )
        logging.debug( 'stderr output:\n' + format_output(x[1]) )
        #out= dict(stdout=x[0], stderr=x[1])
        #return out
        return (x[0], x[1])
