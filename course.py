class Course :
    def __init__(self, name,treiner_name):
        self.name = name,
        self.active=True
        self.num_of_participate=0
        self.treiner_name=treiner_name

    def __repr__(self):
        return f"{self.name} :{self.num_of_participate}"