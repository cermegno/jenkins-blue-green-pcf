import redislite
r = redislite.StrictRedis()
r.set('foo', 'bar')
print r.get('foo')
r.hmset('survey1',{'division':'ENT','state':'NSW','feedback':'hello world'})
r.hmset('survey2',{'division':'COMM','state':'NSW','feedback':'great'})
r.hmset('survey3',{'division':'ENT','state':'VIC','feedback':'awesome'})
for eachsurvey in r.keys('new_survey*'):
    response += "Division : " + r.hget(eachsurvey,'division') + "<br>"
    response += "State    : " + r.hget(eachsurvey,'state') + "<br>"
    response += "Feedback : " + r.hget(eachsurvey,'feedback') + "<br>"
    response += " ----------------------<br>"
print response
