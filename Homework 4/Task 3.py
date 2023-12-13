cats = [('Мартин', 5, 'Алексей', 'Егоров'),
        ('Фродо', 3, 'Анна', 'Самохина'),
        ('Вася', 4, 'Андрей', 'Белов'),
        ('Муся', 7, 'Игорь', 'Бероев'),
        ('Изольда', 2, 'Игорь', 'Бероев'),
        ('Снейп', 1, 'Марина', 'Апраксина'),
        ('Лютик', 4, 'Виталий', 'Соломин'),
        ('Снежок', 3, 'Марина', 'Апраксина'),
        ('Марта', 5, 'Сергей', 'Колесников'),
        ('Буся', 12, 'Алена', 'Федорова'),
        ('Джонни', 10, 'Игорь', 'Андропов'),
        ('Мурзик', 1, 'Даниил', 'Невзоров'),
        ('Барсик', 2, 'Виталий', 'Соломин'),
        ('Рыжик', 7, 'Владимир', 'Медведев'),
        ('Матильда', 8, 'Андрей', 'Белов'),
        ('Гарфилд', 3, 'Александр', 'Березуев')]
new_dir_w_cat = {}
for animal_name, age_of_the_animal, owners_name, owners_last_name in cats:
        owner_key = (owners_name, owners_last_name)
        if owner_key not in new_dir_w_cat:
                new_dir_w_cat[owner_key] = {'Имя' : owners_name, 'Фамилия' : owners_last_name, 'Животные' : []}
                new_dir_w_cat[owner_key]['Животные'].append({'Кличка': animal_name, 'Возраст': age_of_the_animal})
        else:
                new_dir_w_cat[owner_key]['Животные'].append({'Кличка': animal_name, 'Возраст': age_of_the_animal})
# print(new_dir_w_cat) ####

for owner_key in new_dir_w_cat:
        owners_name, owners_last_name = owner_key
        animals_info = new_dir_w_cat[owner_key]['Животные']

        animals_str = '; '.join([f'{info["Кличка"]}, {info["Возраст"]}' for info in animals_info])

        print(f'{owners_name}, {owners_last_name}: {animals_str}')


