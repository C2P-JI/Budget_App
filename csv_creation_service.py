import rpyc
import os
import csv

class CSVservice(rpyc.Service):
    def on_connect(self, conn):
        print("Client connected")
    
    def on_disconnect(self, conn):
        print("Client disconnected")
        
    def create_income_csv(self, path):
        file = path + "/income.csv"
        fields = ['cost','from', 'day', 'month', 'year']

        with open(file, 'w') as csv_file:
            # creating a csv writer object
            csvwriter = csv.writer(csv_file)

            # writing the fields
            csvwriter.writerow(fields)

    def create_bills_csv(self, path):
        file = path + "/bills.csv"
        fields = ['cost', 'description', 'day', 'month', 'year']

        with open(file, 'w') as csv_file:
            csvwriter = csv.writer(csv_file)

            csvwriter.writerow(fields)


    def create_food_csv(self, path):
        file = path + "/food.csv"
        fields = ['cost', 'description', 'day', 'month', 'year']

        with open(file, 'w') as csv_file:
            csvwriter = csv.writer(csv_file)

            csvwriter.writerow(fields)

    def create_shopping_csv(self, path):
        file = path + "/shopping.csv"
        fields = ['cost', 'description', 'day', 'month', 'year']

        with open(file, 'w') as csv_file:
            csvwriter = csv.writer(csv_file)

            csvwriter.writerow(fields)

    def create_entertainment_csv(self, path):
        file = path + "/entertainment.csv"
        fields = ['cost', 'description', 'day', 'month', 'year']

        with open(file, 'w') as csv_file:
            csvwriter = csv.writer(csv_file)

            csvwriter.writerow(fields)

    def create_other_csv(self, path):
        file = path + "/other.csv"
        fields = ['cost', 'description', 'day', 'month', 'year']

        with open(file, 'w') as csv_file:
            csvwriter = csv.writer(csv_file)

            csvwriter.writerow(fields)


    def create_transportation_csv(self, path):
        file = path + "/transportation.csv"
        fields = ['cost', 'description', 'day', 'month', 'year']

        with open(file, 'w') as csv_file:
            csvwriter = csv.writer(csv_file)

            csvwriter.writerow(fields)

    def exposed_create_db(self, user):
        folder_name = str(user)
        path = 'user_db/' + folder_name
        os.mkdir(path)

        self.create_income_csv(path)
        self.create_bills_csv(path)
        self.create_food_csv(path)
        self.create_shopping_csv(path)
        self.create_entertainment_csv(path)
        self.create_other_csv(path)
        self.create_transportation_csv(path)


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(CSVservice, port=18862)
    server.start()
