import sys

print('Content-Type: text/plain; charset=UTF-8')
print('Status: 200')
print()

print('Hello from python on', sys.platform)

print()
print('### Arguments ###')
print()

print(sys.argv)

args = sys.argv
if len(args) > 1:
    print('You have just sent the following args as GET parameters!')
    print()
    print(sys.argv[1:])
    
    arg1 = args[1].split('=')[1]
    print(int(arg1) + 1)
else:
    print('You gave me no parameters :(')
