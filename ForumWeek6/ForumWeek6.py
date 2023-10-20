import math

# Read the data from the file
def read_data(file_name):
    with open(file_name, 'r') as file:
        data = [line.strip().split() for line in file.readlines()]
        return data

# Separate the data into features and labels
def separate_data(data):
    features = [line[:-1] for line in data]
    labels = [line[-1] for line in data]
    return features, labels

# Define the features we want to predict for
day = 'Weekday'
discount = 'No'
delivery = 'Yes'

# Calculate the probabilities for each outcome
def calculate_probabilities(features, labels, day, discount, delivery):
    purchase_count = 0
    not_purchase_count = 0
    total_count = len(labels)

    for i in range(total_count):
        if features[i][0] == day and features[i][1] == discount and features[i][2] == delivery:
            if labels[i] == 'Yes':
                purchase_count += 1
            else:
                not_purchase_count += 1

    purchase_prob = purchase_count / total_count
    not_purchase_prob = not_purchase_count / total_count

    return purchase_prob, not_purchase_prob

# Print the probabilities for each outcome
def print_probabilities(purchase_prob, not_purchase_prob, day, discount, delivery):
    print('Probabilities for the given combination of features:')
    print('- Day =', day)
    print('- Discount =', discount)
    print('- Delivery =', delivery)
    print('- Purchase:', purchase_prob)
    print('- Not Purchase:', not_purchase_prob)

def main():
    file_name = 'ForumDataSet.txt'
    try:
        data = read_data(file_name)
        features, labels = separate_data(data)
        purchase_prob, not_purchase_prob = calculate_probabilities(features, labels, day, discount, delivery)
        print_probabilities(purchase_prob, not_purchase_prob, day, discount, delivery)
    except FileNotFoundError:
        print(f"{file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()