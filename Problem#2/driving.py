def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   #write your code here
    gallons = miles_driven/miles_per_gallon
    dollars = gallons * dollars_per_gallon
    print(f'{dollars:.2f}')

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    #print your costs here like example below
    #print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')


    counter = 3
    while counter == 3:
      driving_cost(miles_per_gallon, dollars_per_gallon, 10)
      counter = 2
    while counter == 2:
      driving_cost(miles_per_gallon, dollars_per_gallon, 50)
      counter = 1
    while counter == 1 :
      driving_cost(miles_per_gallon, dollars_per_gallon, 400)
      counter = 0
   