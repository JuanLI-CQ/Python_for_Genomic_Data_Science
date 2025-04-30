# use the call() function in the subprocess module to run an external program
import subprocess
subprocess.call(["ls", "-l"])

# return code: indicates the success or failure of the execution

subprocess.call(["tophat", "genome_mouse_idx", "PE_reads_1.fq.gz", "PE_reads_2.fq.gz"])