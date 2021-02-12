'''
(py_37_ds) YuLong@MacBook-Pro:~/Desktop/Working_Area/recsys_im$ python absl_exmaple.py --quantize_mode abc
'''
from absl import app, flags, logging
from absl.flags import FLAGS

flags.DEFINE_string('weights', './checkpoints/yolov4-416',
                    'path to weights file')
flags.DEFINE_string(
    'output', './checkpoints/yolov4-416-fp32.tflite', 'path to output')
flags.DEFINE_integer('input_size', 416, 'path to output')
flags.DEFINE_string('quantize_mode', 'float32',
                    'quantize mode (int8, float16, float32)')
flags.DEFINE_string(
    'dataset', 'ml-20m/ratings.csv', 'path to dataset')


def print_flag():
    print(dir(FLAGS))
    print(FLAGS.quantize_mode)
    print(FLAGS.input_size)
    print(FLAGS.dataset)


def main(_argv):
    print_flag()


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
