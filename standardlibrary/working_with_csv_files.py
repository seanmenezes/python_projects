import csv

with open("data.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id","product_id","price"])
    writer.writerow([1000,1,5])
    writer.writerow([1001,2,15])
    writer.writerow([1003,3,21])
    writer.writerow([1004,4,7])