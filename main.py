import gspread, re, sys
from oauth2client.service_account import ServiceAccountCredentials

EMPTY_STRING = ''

def main(kwargs: dict):
    # get spreadsheet info
    url = kwargs.get('--url', kwargs.get('-u', EMPTY_STRING))

    # create client using google client secret
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    # open spreadsheet
    spreadsheet = client.open_by_url(url)
    sheet = spreadsheet.get_worksheet(0)

    # print stuff
    records = sheet.get_all_values()
    print(records)

if __name__ == '__main__':
    tuples = [(sys.argv[i], sys.argv[i+1]) for i in range(1, len(sys.argv), 2)]
    kwargs = dict(tuples)
    main(kwargs)
