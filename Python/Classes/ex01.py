class User:
    def __init__(self, nome, plan, email):
        self.nome = nome
        self.plan = plan
        self.email = email
        self.list_plans = ['basic', 'plus']
        if plan in self.list_plans:
            self.plan = plan
        else:
            raise Exception("Plano inválido")
        

    def change_plan(self, new_plan):
        if new_plan in self.list_plans:
            self.plan = new_plan
        else:
            raise Exception("Plan invalidad")
        

    def see_film(self, film, plano_filme):
        if self.plan in plano_filme:
            print(f"Ver fime :{film}")
        elif self.plan == "plus":
            print(f"Ver fime :{film}")
        elif plano_filme == "plus" and self.plan == "basic":
            print("Aprimmore o seu plano para assitir esse filme")
        else:
            print("plan invalid")

user1 = User("João", "basic", "joao@email")
print(user1.plan)


print(user1.plan)
user1.see_film("Velozes e furiosos", "plus")
user1.change_plan('plus')
user1.see_film("Velozes e furiosos", "plus")