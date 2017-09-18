import sys
def tuples(diction):
    sys.stdout.write('[')
    for key, data in diction.iteritems():
        sys.stdout.write( '("' + key + '", "' + data + '")')
        sys.stdout.write(' ')
    sys.stdout.write(']')
    sys.stdout.flush()
# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
#[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
tuples(my_dict)
