from absl import flags
FLAGS = flags.FLAGS

flags.DEFINE_string('myflag', 'Some default string', 'The value of myflag.')

def main(argv):
  if FLAGS.debug:
    print('non-flag arguments:', argv)
  print('The value of myflag is %s' % FLAGS.myflag)


if __name__ == '__main__':
  main()
