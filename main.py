import requests
import datetime


def callback(): 
    return 'xxxxxxxxx'

def main():
    data = callback()
    now = datetime.datetime.now()
    # now = now.strftime("%Y-%m-%d")
    timestemp = now

    print(timestemp)

    try:
        resp = requests.get('http://api.plos.org/search?q=title:DNA')
        if resp.status_code != 200:
            print(format(resp.status_code))

        # print(resp.json())

        # for todo_item in resp.json():
            # print('{} {}'.format(todo_item['id'], todo_item['summary']))
        # print(data)
    except Exception as e: 
        print(e)


if __name__ == "__main__":
    main()




