
'''
@ind.route('/showdetail/<string:userid>', methods=['GET', 'POST'])
def showdetail(userid):

    data = sqlhelper.fetch_all("SELECT id,line , datrtime FROM  coderecord WHERE user_id = %s;",(userid,))
    print('data',data)
    line = []
    for i in data:
        if 'line' in i:
            line.append(int(i['line']))
    print('line',line)

    name = []
    for i in data:
        if 'userName' in i:
            name.append(i['userName'])


    new_data = [{'name': list(set(name)),'data': line}]
    print('newwwwww',new_data)
    return render_template('showdetail.html', data=data, new_data = json.dumps(new_data))
'''