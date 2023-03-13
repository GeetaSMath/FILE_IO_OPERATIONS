import csv

with open('csv_file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "scholl", "nameo_student"])
    writer.writerow([1, "A", "abc"])
    writer.writerow([2, "B", "XYZ"])