
import sys
import statiz_background2 as stb

year = sys.argv[1]

statiz_crawling = stb.Statiz()
statiz_crawling.record_site(year)
statiz_crawling.kt_site(year)
statiz_crawling.export_excel(year)

print('Process Done!')