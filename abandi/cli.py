from subprocess import PIPE, Popen
import logging


def call(cmd, dryrun=False):
    logging.debug( 'calling:' )
    logging.debug( cmd )
    if not dryrun:
        pop= Popen(cmd, stdout=PIPE,stderr=PIPE, shell=1)
        x= pop.communicate()
        def format_output(s):
            s=s.replace('\x08',' ') # for unrar in eclipse
            return s
        logging.debug( 'returncode:' + str(pop.returncode) )
        logging.debug( 'stdout output:\n' + format_output(x[0]) )
        logging.debug( 'stderr output:\n' + format_output(x[1]) )

        return (x[0], x[1], pop.returncode)
