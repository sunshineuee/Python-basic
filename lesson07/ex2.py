import yaml
import os

d = {'my_project':
    [{'settings': [
        '__init__.py', 'dev.py', 'prod.py'
    ],
    },
        {'mainapp': [
            '__init__.py', 'models.py', 'views.py', {'templates': [{
                'mainapp': ['base.html', 'index.html']}]
            }]},
        {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{
            'authapp': ['base.html', 'index.html']}]
        }
                     ]
         }
    ]
}
f = open('config.yaml', 'w')
f.write(yaml.dump(d))
f.close()

with open("config.yaml") as y_file:
    d = yaml.safe_load(y_file)


def create_data(data, prefix=""):
    for folder, data_tmps in data.items():
        full_path = os.path.join(prefix, folder)
        os.makedirs(full_path, exist_ok=True)
        if isinstance(data_tmps, dict):
            create_data(data_tmps, full_path)
        for data_tmp in data_tmps:
            if isinstance(data_tmp, dict):
                create_data(data_tmp, full_path)
            elif isinstance(data_tmp, str):
                        with open(os.path.join(full_path, data_tmp), 'w') as _:
                            pass


create_data(d)