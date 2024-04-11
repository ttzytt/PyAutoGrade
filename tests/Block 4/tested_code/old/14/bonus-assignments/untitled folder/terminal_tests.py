import subprocess
result = subprocess.run(['mkdir', 'test'], stdout=subprocess.PIPE)
print(result.stdout.decode())
