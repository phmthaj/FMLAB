# TODO: [part d]
# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import argparse
import utils

def main():
    accuracy = 0.0

    # Compute accuracy in the range [0.0, 100.0]
    ### YOUR CODE HERE ###
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev_path', default='birth_dev.tsv')
    args = parser.parse_args()
    with open(args.dev_path, encoding='utf-8') as fin:
        lines = [x.strip() for x in fin if x.strip()]
    predictions = ['London' for _ in lines]
    total, correct = utils.evaluate_places(args.dev_path, predictions)
    accuracy = 0.0 if total == 0 else correct / total * 100.0
    return accuracy
    ### END YOUR CODE ###

    return accuracy

if __name__ == '__main__':
    accuracy = main()
    with open("london_baseline_accuracy.txt", "w", encoding="utf-8") as f:
        f.write(f"{accuracy}\n")
