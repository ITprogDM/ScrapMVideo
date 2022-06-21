import requests
import json


def get_data():
    import requests

    cookies = {
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'MAIN_PAGE_VARIATION_1': '2',
        'MVID_2_exp_in_1': '6',
        'MVID_AB_SERVICES_DESCRIPTION': 'var2',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_30347',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '20907494208',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '5000003600000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '2',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_LOGIN': 'true',
        'MVID_NEW_LK_MENU_BUTTON': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'old',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PICKUP_SEAMLESS_AB_TEST': '2',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'searchType2': '1',
        'admitad_deduplication_cookie': 'yandex.ru__organic',
        '__SourceTracker': 'yandex.ru__organic',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        'tmr_lvidTS': '1655632725710',
        'tmr_lvid': 'e259cb7fe5dc24854508ed598fcbca15',
        '_ym_uid': '165563272640650234',
        '_ym_d': '1655632726',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '4b5fca10-838b-41db-b387-5f1ef3b4d26b',
        'st_uid': '547dc054479111c0e0ee2ba8338e6277',
        'advcake_track_id': '99b3741f-14f7-9922-2481-cada981698d7',
        'advcake_session_id': '0d370fde-f786-3f59-f8b2-e0bfc1f01e6d',
        'uxs_uid': '68ef43c0-efb6-11ec-8d8c-83c84923c78c',
        'flocktory-uuid': '7aa69232-2bb6-41df-b2a5-e0f4cf2c4177-2',
        'afUserId': 'bd296d6e-199c-406a-8012-786f76d40c84-p',
        'AF_SYNC': '1655632726731',
        'adrcid': 'AI54TfjTVpRP_s72ynjmecw',
        'flacktory': 'no',
        'SMSError': '',
        'authError': '',
        '_gid': 'GA1.2.1681973805.1655830217',
        '_ym_isad': '2',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80': '2433014794.20480.0000',
        'bIPs': '53593859',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        'BIGipServeratg-ps-prod_tcp80_clone': '2433014794.20480.0000',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VJDCpbLRdbQQwhdSkqOlRADyUPGRQgcHNzHz1ELTUNXRtTdR1pJEYwE34WaWE9UXJ1EQ0PGjhrImFOXyFMWFRqJh8WfHMmTwkQYkNIc2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC5DaB1hUGIhRVhJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=cTICPA==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VJDCpbLRdbQQwhdSkqOlRADyUPGRQgcHNzHz1ELTUNXRtTdR1pJEYwE34WaWE9UXJ1EQ0PGjhrImFOXyFMWFRqJh8WfHMmTwkQYkNIc2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC5DaB1hUGIhRVhJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=cTICPA==',
        'cfidsgib-w-mvideo': 'u1LPbFb01/DnIOlTmXterFNRBONpw5gQulB6xVPjnAs1I66GZUFeKs9vB5/vkoiCb1ISVbTrYQWWzzuQSgB6vVO95AqTi7g6QCe3c7VUTJJ3U7FJfMykH4x4b6Egyw7yJKQnVJwHR1yfIGqR73xlQhGVvU8h3L50JGw1lA==',
        'cfidsgib-w-mvideo': 'u1LPbFb01/DnIOlTmXterFNRBONpw5gQulB6xVPjnAs1I66GZUFeKs9vB5/vkoiCb1ISVbTrYQWWzzuQSgB6vVO95AqTi7g6QCe3c7VUTJJ3U7FJfMykH4x4b6Egyw7yJKQnVJwHR1yfIGqR73xlQhGVvU8h3L50JGw1lA==',
        'gsscgib-w-mvideo': '1CiQONLRs/V0kfhChCLk3tFQdixhC6AbW3CxSu/xHV4+vUxj1rNGCrCX5QMFhQA013OwOIESfIYSW6PTgTILargfWorbhA6PyYvSUMxCZDE/1CqEXuuz0YHfF03by8DIhv2R5JV8aVidtTK2hberx67MOHlR6QvL2SFMWShMLi3zAb5W+C2gCwkvvY5ZKDz81aTwkcT1SNGg76vjBDp9bjpbIr1bUer5C2jGVuJ/i6FxUK25XbEVyKDFtW2KNw==',
        'gsscgib-w-mvideo': '1CiQONLRs/V0kfhChCLk3tFQdixhC6AbW3CxSu/xHV4+vUxj1rNGCrCX5QMFhQA013OwOIESfIYSW6PTgTILargfWorbhA6PyYvSUMxCZDE/1CqEXuuz0YHfF03by8DIhv2R5JV8aVidtTK2hberx67MOHlR6QvL2SFMWShMLi3zAb5W+C2gCwkvvY5ZKDz81aTwkcT1SNGg76vjBDp9bjpbIr1bUer5C2jGVuJ/i6FxUK25XbEVyKDFtW2KNw==',
        'fgsscgib-w-mvideo': '06iA8f834f9b83960b859d88dcb1325e7b2640e0',
        'fgsscgib-w-mvideo': '06iA8f834f9b83960b859d88dcb1325e7b2640e0',
        'cfidsgib-w-mvideo': 'zErqv13SC0pRXkgcXKifGICO0r/7+fTsSTrj4A8kNsXNC2u09D9xCWuYpf4RNqaJQvBUyVB3tImfrvMGc+i6CgPbjpuSebQzHy1OzF3gM8SueN5NkX3vaSNipiISOKQFGbCxpbFIB98agjKKd+KWJ+cd9V+kZrNQB5RFJQ==',
        'CACHE_INDICATOR': 'false',
        'mindboxDeviceUUID': 'db15de63-e14a-40aa-9f84-d25d0aea7229',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22db15de63-e14a-40aa-9f84-d25d0aea7229%22%7D',
        '__lhash_': 'cc09820b5d89979fbbe0d3de52f0a203',
        'MVID_ENVCLOUD': 'primary',
        '_dc_gtm_UA-1873769-1': '1',
        '_ga': 'GA1.2.1903879300.1655632726',
        '_dc_gtm_UA-1873769-37': '1',
        'tmr_detect': '0%7C1655831815437',
        'JSESSIONID': '5yChvx9Qhxyjrv7vTTCFJ2kTJnw192PZ2yxLymmnvZJTLzkxvndD!-652762937',
        'tmr_reqNum': '100',
        '_ga_CFMZTSS5FM': 'GS1.1.1655830216.2.1.1655831857.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1655830216.2.1.1655831857.15',
        'ADRUM_BT': 'R:88|g:9113517f-ae3a-440e-88d2-e206f4de7335934479',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; MAIN_PAGE_VARIATION_1=2; MVID_2_exp_in_1=6; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_30347; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=20907494208; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=5000003600000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=2; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_MENU_BUTTON=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=old; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; searchType2=1; admitad_deduplication_cookie=yandex.ru__organic; __SourceTracker=yandex.ru__organic; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; tmr_lvidTS=1655632725710; tmr_lvid=e259cb7fe5dc24854508ed598fcbca15; _ym_uid=165563272640650234; _ym_d=1655632726; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=4b5fca10-838b-41db-b387-5f1ef3b4d26b; st_uid=547dc054479111c0e0ee2ba8338e6277; advcake_track_id=99b3741f-14f7-9922-2481-cada981698d7; advcake_session_id=0d370fde-f786-3f59-f8b2-e0bfc1f01e6d; uxs_uid=68ef43c0-efb6-11ec-8d8c-83c84923c78c; flocktory-uuid=7aa69232-2bb6-41df-b2a5-e0f4cf2c4177-2; afUserId=bd296d6e-199c-406a-8012-786f76d40c84-p; AF_SYNC=1655632726731; adrcid=AI54TfjTVpRP_s72ynjmecw; flacktory=no; SMSError=; authError=; _gid=GA1.2.1681973805.1655830217; _ym_isad=2; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80=2433014794.20480.0000; bIPs=53593859; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; BIGipServeratg-ps-prod_tcp80_clone=2433014794.20480.0000; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VJDCpbLRdbQQwhdSkqOlRADyUPGRQgcHNzHz1ELTUNXRtTdR1pJEYwE34WaWE9UXJ1EQ0PGjhrImFOXyFMWFRqJh8WfHMmTwkQYkNIc2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC5DaB1hUGIhRVhJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=cTICPA==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VJDCpbLRdbQQwhdSkqOlRADyUPGRQgcHNzHz1ELTUNXRtTdR1pJEYwE34WaWE9UXJ1EQ0PGjhrImFOXyFMWFRqJh8WfHMmTwkQYkNIc2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC5DaB1hUGIhRVhJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=cTICPA==; cfidsgib-w-mvideo=u1LPbFb01/DnIOlTmXterFNRBONpw5gQulB6xVPjnAs1I66GZUFeKs9vB5/vkoiCb1ISVbTrYQWWzzuQSgB6vVO95AqTi7g6QCe3c7VUTJJ3U7FJfMykH4x4b6Egyw7yJKQnVJwHR1yfIGqR73xlQhGVvU8h3L50JGw1lA==; cfidsgib-w-mvideo=u1LPbFb01/DnIOlTmXterFNRBONpw5gQulB6xVPjnAs1I66GZUFeKs9vB5/vkoiCb1ISVbTrYQWWzzuQSgB6vVO95AqTi7g6QCe3c7VUTJJ3U7FJfMykH4x4b6Egyw7yJKQnVJwHR1yfIGqR73xlQhGVvU8h3L50JGw1lA==; gsscgib-w-mvideo=1CiQONLRs/V0kfhChCLk3tFQdixhC6AbW3CxSu/xHV4+vUxj1rNGCrCX5QMFhQA013OwOIESfIYSW6PTgTILargfWorbhA6PyYvSUMxCZDE/1CqEXuuz0YHfF03by8DIhv2R5JV8aVidtTK2hberx67MOHlR6QvL2SFMWShMLi3zAb5W+C2gCwkvvY5ZKDz81aTwkcT1SNGg76vjBDp9bjpbIr1bUer5C2jGVuJ/i6FxUK25XbEVyKDFtW2KNw==; gsscgib-w-mvideo=1CiQONLRs/V0kfhChCLk3tFQdixhC6AbW3CxSu/xHV4+vUxj1rNGCrCX5QMFhQA013OwOIESfIYSW6PTgTILargfWorbhA6PyYvSUMxCZDE/1CqEXuuz0YHfF03by8DIhv2R5JV8aVidtTK2hberx67MOHlR6QvL2SFMWShMLi3zAb5W+C2gCwkvvY5ZKDz81aTwkcT1SNGg76vjBDp9bjpbIr1bUer5C2jGVuJ/i6FxUK25XbEVyKDFtW2KNw==; fgsscgib-w-mvideo=06iA8f834f9b83960b859d88dcb1325e7b2640e0; fgsscgib-w-mvideo=06iA8f834f9b83960b859d88dcb1325e7b2640e0; cfidsgib-w-mvideo=zErqv13SC0pRXkgcXKifGICO0r/7+fTsSTrj4A8kNsXNC2u09D9xCWuYpf4RNqaJQvBUyVB3tImfrvMGc+i6CgPbjpuSebQzHy1OzF3gM8SueN5NkX3vaSNipiISOKQFGbCxpbFIB98agjKKd+KWJ+cd9V+kZrNQB5RFJQ==; CACHE_INDICATOR=false; mindboxDeviceUUID=db15de63-e14a-40aa-9f84-d25d0aea7229; directCrm-session=%7B%22deviceGuid%22%3A%22db15de63-e14a-40aa-9f84-d25d0aea7229%22%7D; __lhash_=cc09820b5d89979fbbe0d3de52f0a203; MVID_ENVCLOUD=primary; _dc_gtm_UA-1873769-1=1; _ga=GA1.2.1903879300.1655632726; _dc_gtm_UA-1873769-37=1; tmr_detect=0%7C1655831815437; JSESSIONID=5yChvx9Qhxyjrv7vTTCFJ2kTJnw192PZ2yxLymmnvZJTLzkxvndD!-652762937; tmr_reqNum=100; _ga_CFMZTSS5FM=GS1.1.1655830216.2.1.1655831857.0; _ga_BNX5WPP3YK=GS1.1.1655830216.2.1.1655831857.15; ADRUM_BT=R:88|g:9113517f-ae3a-440e-88d2-e206f4de7335934479',
        'referer': 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Yandex";v="22"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.2.615 Yowser/2.5 Safari/537.36',
        'x-set-application-id': 'e37daccb-b7db-4de2-94f7-79de93c8d6aa',
    }

    params = {
        'categoryId': '205',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    print(response)

    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    #print(products_ids)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    #print(len(response.get('body').get('products')))

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)


    items_prices ={}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')

        items_prices[item_id] = {
            'item_basePrice' : item_base_price,
            'item_sale_price': item_sale_price
        }

    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)

def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()



