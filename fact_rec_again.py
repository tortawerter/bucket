num_fact = int(input())


def fact_rec_again(num_fact):
    if num_fact == 0:
        return 1
    else:
        return fact_rec_again(num_fact - 1) * num_fact


print(fact_rec_again(num_fact))
