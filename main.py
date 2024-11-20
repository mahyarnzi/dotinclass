import functions
import configuration

name = configuration.name
family = configuration.family
fullname = functions.fullname(name, family)

print(fullname)

