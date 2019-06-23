import subprocess
import sys

sys.stdout = open('out.txt', 'w')

subprocess.call(["git", "rev-list","--left-right","--count","master...dev"])

