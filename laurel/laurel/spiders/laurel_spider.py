from urllib.parse import urlparse
from scrapy.http import Request
import scrapy

class LaurelSpider(scrapy.Spider):
    name = "laurel"

    allowed_domains = [
        "www.cityoflaurel.org",
        "files.cityoflaurel.org",
        "dat.maryland.gov"
    ]

    start_urls = [
        "https://www.cityoflaurel.org/baps/jobs/application-process/",
        "https://www.cityoflaurel.org/baps/audit-reports/",
        "https://www.cityoflaurel.org/baps/city-budgets/",
        "https://www.cityoflaurel.org/baps/jobs/employee-benefits/",
        "https://www.cityoflaurel.org/baps/jobs/",
        "https://www.cityoflaurel.org/baps/mayors-summer-jobs-program/",
        "https://www.cityoflaurel.org/baps/projects/",
        "https://www.cityoflaurel.org/baps/tax-information/",
        "https://www.cityoflaurel.org/comm/cable-franchise-liason/",
        "https://www.cityoflaurel.org/comm/contacts-hours/",
        "https://www.cityoflaurel.org/comm/digital-signage-use-non-profit-groups-laurel/",
        "https://www.cityoflaurel.org/comm/visitor-information/dining/",
        "https://www.cityoflaurel.org/comm/email-subscribe/",
        "https://www.cityoflaurel.org/comm/visitor-information/health-and-fitness/",
        "https://www.cityoflaurel.org/comm/visitor-information/hotels/",
        "https://www.cityoflaurel.org/comm/laurel-tv/",
        "https://www.cityoflaurel.org/comm/press-releases/",
        "https://www.cityoflaurel.org/comm/publications/",
        "https://www.cityoflaurel.org/comm/passport-office/",
        "https://www.cityoflaurel.org/comm/press-kits/",
        "https://www.cityoflaurel.org/comm/visitor-information/shopping/",
        "https://www.cityoflaurel.org/comm/social-media-center/",
        "https://www.cityoflaurel.org/comm/visitor-information/about-laurel-and-its-history/city-seal/",
        "https://www.cityoflaurel.org/comm/visitor-information/transportation/",
        "https://www.cityoflaurel.org/comm/visitor-information/",
        "https://www.cityoflaurel.org/comm/volunteering/",
        "https://www.cityoflaurel.org/ecd/affordable-housing-program/",
        "https://www.cityoflaurel.org/ecd/arts-and-entertainment-district/",
        "https://www.cityoflaurel.org/ecd/city-limits-and-addresses/",
        "https://www.cityoflaurel.org/permits/bulletins/",
        "https://www.cityoflaurel.org/ecd/economic-development-commercial-corridor-program/",
        "https://www.cityoflaurel.org/ecd/main-street-development-programs/main-street-business-relocation-grant-program/",
        "https://www.cityoflaurel.org/ecd/main-street-development-programs/main-street-commercial-property-improvement-program/",
        "https://www.cityoflaurel.org/ecd/main-street-development-programs/",
        "https://www.cityoflaurel.org/ecd/main-street-development-programs/main-street-retail-storefront-fa%C3%A7ade-improvement-program/",
        "https://www.cityoflaurel.org/ecd/main-street-development-programs/main-street-sign-grant-program/",
        "https://www.cityoflaurel.org/ecd/planning/",
        "https://www.cityoflaurel.org/ecd/unified-land-development-code/",
        "https://www.cityoflaurel.org/ecd/planning/zoning-applications/",
        "https://www.cityoflaurel.org/em/emergency-resources/all-hazards-plan/",
        "https://www.cityoflaurel.org/em/alerts/",
        "https://www.cityoflaurel.org/em/emergency-resources/emergency-evacuation-route/",
        "https://www.cityoflaurel.org/em/emergency-operations-center-eoc/",
        "https://www.cityoflaurel.org/em/emergency-resources/emergency-operations-guide/",
        "https://www.cityoflaurel.org/em/emergency-resources/",
        "https://www.cityoflaurel.org/em/emergency-resources/flood-zone-map/",
        "https://www.cityoflaurel.org/em/get-emergency-notifications/",
        "https://www.cityoflaurel.org/em/emergency-resources/make-kit/",
        "https://www.cityoflaurel.org/em/partners/",
        "https://www.cityoflaurel.org/em/emergency-resources/specialized-vehicles/",
        "https://www.cityoflaurel.org/weather-related-emergencies/",
        "https://www.cityoflaurel.org/it/gis/",
        "https://www.cityoflaurel.org/it/it-internships/",
        "https://www.cityoflaurel.org/it/gis/maps/",
        "https://www.cityoflaurel.org/it/mylaurel-mobile-app/",
        "https://www.cityoflaurel.org/it/web-site-services/",
        "https://www.cityoflaurel.org/mayor/ceremonial-documents/",
        "https://www.cityoflaurel.org/mayor/community-outreach-programs/chow-down-mayor/",
        "https://www.cityoflaurel.org/mayor/community-outreach-programs/",
        "https://www.cityoflaurel.org/mayor/mayors-office-programs/hometown-heroes-%E2%80%93-honorary-banner-recognition-program/",
        "https://www.cityoflaurel.org/mayor/community-outreach-programs/mayors-city-hall-park/",
        "https://www.cityoflaurel.org/mayor/mayors-office-programs/",
        "https://www.cityoflaurel.org/mayor/community-outreach-programs/mayor%E2%80%99s-golden-shovel-award-program/",
        "https://www.cityoflaurel.org/mayor/community-outreach-programs/my-time-mayor-program/",
        "https://www.cityoflaurel.org/ca/insurance-program/",
        "https://www.cityoflaurel.org/clerk/elections-and-voter-registration/",
        "https://www.cityoflaurel.org/clerk/elections-and-voter-registration/voting-wards-and-polling-places/",
        "https://www.cityoflaurel.org/parks/facilities/adopt-park-program/",
        "https://www.cityoflaurel.org/parks/adult-sports-activities/adult-basketball/",
        "https://www.cityoflaurel.org/parks/adult-sports-activities/adult-softball/",
        "https://www.cityoflaurel.org/parks/adult-sports-activities/",
        "https://www.cityoflaurel.org/parks/classes-and-registration/",
        "https://www.cityoflaurel.org/parks/community-initiative-grant-program/",
        "https://www.cityoflaurel.org/parks/facilities/",
        "https://www.cityoflaurel.org/parks/facilities/facility-rentals/",
        "https://www.cityoflaurel.org/parks/featured-events/",
        "https://www.cityoflaurel.org/parks/laurel-teen-outdoors-club/",
        "https://www.cityoflaurel.org/parks/facilities/report-park-vandalism-or-repair-needs/",
        "https://www.cityoflaurel.org/parks/senior-services/",
        "https://www.cityoflaurel.org/parks/facilities/services-provided/",
        "https://www.cityoflaurel.org/parks/youth-sports-activities/",
        "https://www.cityoflaurel.org/police/administration/",
        "https://www.cityoflaurel.org/police/community-info/alarms-residential-and-commercial/",
        "https://www.cityoflaurel.org/police/community-info/amber-alert-program/",
        "https://www.cityoflaurel.org/police/administration/animal-control/",
        "https://www.cityoflaurel.org/police/administration/auxiliary-policevolunteers/",
        "https://www.cityoflaurel.org/police/charity-events/",
        "https://www.cityoflaurel.org/police/chief/",
        "https://www.cityoflaurel.org/police/administration/citizens-police-academy/",
        "https://www.cityoflaurel.org/police/administration/community-policing-unit/",
        "https://www.cityoflaurel.org/police/community-info/",
        "https://www.cityoflaurel.org/police/contact-us/",
        "https://www.cityoflaurel.org/police/community-info/crime-reports/",
        "https://www.cityoflaurel.org/police/education-safety-programs/dare/",
        "https://www.cityoflaurel.org/police/chief/deputy-chief-police/",
        "https://www.cityoflaurel.org/police/community-info/charity-events/fingerprinting-services/",
        "https://www.cityoflaurel.org/police/administration/general-orders/",
        "https://www.cityoflaurel.org/police/administration/law-enforcement-explorer-post-1870/",
        "https://www.cityoflaurel.org/police/chief/mission-and-organizational-values/",
        "https://www.cityoflaurel.org/police/community-info/neighborhood-watch-program/",
        "https://www.cityoflaurel.org/police/administration/obtain-reportpay-citation/",
        "https://www.cityoflaurel.org/police/operations/officer-worn-cameras/",
        "https://www.cityoflaurel.org/police/community-info/other-resources/",
        "https://www.cityoflaurel.org/police/administration/parking-enforcement/",
        "https://www.cityoflaurel.org/police/operations/",
        "https://www.cityoflaurel.org/police/administration/communications/",
        "https://www.cityoflaurel.org/police/recruitment/",
        "https://www.cityoflaurel.org/police/contact-us/report-tip/",
        "https://www.cityoflaurel.org/police/operations/ride-long-program/",
        "https://www.cityoflaurel.org/police/community-info/safety-tips/",
        "https://www.cityoflaurel.org/police/social-media/",
        "https://www.cityoflaurel.org/police/specops/",
        "https://www.cityoflaurel.org/police/operations/specialized-patrol-units/",
        "https://www.cityoflaurel.org/police/community-info/speed-redlight-camera-information/",
        "https://www.cityoflaurel.org/police/community-info/statistics/",
        "https://www.cityoflaurel.org/dpw/active-projects/",
        "https://www.cityoflaurel.org/dpw/bikeway-master-plan/",
        "https://www.cityoflaurel.org/dpw/trash-collection-and-bulk-pickup/bulk-pickup-request/",
        "https://www.cityoflaurel.org/dpw/whats-new/current-road-closures/",
        "https://www.cityoflaurel.org/dpw/projects-bid/",
        "https://www.cityoflaurel.org/dpw/hazardous-waste-disposal/",
        "https://www.cityoflaurel.org/dpw/leaf-collection/",
        "https://www.cityoflaurel.org/dpw/mosquito-control-program/",
        "https://www.cityoflaurel.org/dpw/public-works-schedule/",
        "https://www.cityoflaurel.org/dpw/recycling-program/recycle-coach/",
        "https://www.cityoflaurel.org/dpw/recycling-program/",
        "https://www.cityoflaurel.org/dpw/trash-collection-and-bulk-pickup/residential-collection/",
        "https://www.cityoflaurel.org/dpw/sidewalks/",
        "https://www.cityoflaurel.org/dpw/snow-removal/",
        "https://www.cityoflaurel.org/dpw/storm-drains/",
        "https://www.cityoflaurel.org/dpw/street-repair/",
        "https://www.cityoflaurel.org/dpw/traffic-safety/",
        "https://www.cityoflaurel.org/dpw/trash-collection-and-bulk-pickup/",
        "https://www.cityoflaurel.org/dpw/tree-management/",
        "https://www.cityoflaurel.org/dpw/water-and-sewer/",
        "https://www.cityoflaurel.org/dpw/whats-new/",
        "https://www.cityoflaurel.org/dpw/whos-who-public-works/",
        "https://www.cityoflaurel.org/dpw/yard-waste/",
        "https://www.cityoflaurel.org/dpw/yard-waste/yard-waste-pickup-request/",
        "https://www.cityoflaurel.org/clerk/meetings/about-mayor%C2%A0and-city-council-meetings-and-work-sessions/",
        "https://www.cityoflaurel.org/boards/boards/",
        "https://www.cityoflaurel.org/boards/cacs/",
        "https://www.cityoflaurel.org/boards/commissions/",
        "https://www.cityoflaurel.org/clerk/legislation-and-executive-orders/",
        "https://www.cityoflaurel.org/clerk/maryland-public-information-act-mpia-requests/",
        "https://www.cityoflaurel.org/clerk/meetings/",
        "https://www.cityoflaurel.org/clerk/municipal-code-and-city-charter/",
        "https://www.cityoflaurel.org/clerk/recent-committee-reports/",
        "https://www.cityoflaurel.org/permits/permits/browse/",
        "https://www.cityoflaurel.org/permits/business-licenses/",
        "https://www.cityoflaurel.org/permits/permits/city-impact-fees/",
        "https://www.cityoflaurel.org/permits/foreclosure-registration-program/",
        "https://www.cityoflaurel.org/permits/inspections/",
        "https://www.cityoflaurel.org/permits/permits/new-commercial-construction-checklist/",
        "https://www.cityoflaurel.org/permits/online-payments/",
        "https://www.cityoflaurel.org/permits/permits/",
        "https://www.cityoflaurel.org/permits/pet-licensing/",
        "https://www.cityoflaurel.org/permits/code-enforcement/",
        "https://www.cityoflaurel.org/permits/permits/residential/"
    ]

    def parse(self, response):
        base_url = 'https://www.cityoflaurel.org'
        links_with_dupes = response.css('div#site-main')[0].css('a').xpath('@href').extract()
        links = list(set(links_with_dupes))
        for link in links:
            print("LINK: " + link + '\n')
            if link.endswith('.pdf'):
                link = urlparse.urljoin(base_url, link)
                yield Request(url=link, callback=self.save_pdf)
            if "http" not in str(link):
                yield Request(url=base_url + link + '/', callback=self.third_pass)
            elif "cityoflaurel" in link:
                yield Request(url=link, callback=self.third_pass)
            else:
                yield { "link": link }


    def second_pass(self, response):
        base_url = 'https://www.cityoflaurel.org'
        links_with_dupes = response.css('div#site-main')[0].css('section#site-content')[0].css('a').xpath('@href').extract()
        links = list(set(links_with_dupes))
        for link in links:
            print("LINK: " + link + '\n')
            if link.endswith('.pdf'):
                link = urlparse.urljoin(base_url, link)
                yield Request(url=link, callback=self.save_pdf)
            if "http" not in str(link):
                yield Request(url=base_url + link + '/', callback=self.third_pass)
            elif "cityoflaurel" in link:
                yield Request(url=link, callback=self.third_pass)
            else:
                yield { "link": link }

    def third_pass(self, response):
        base_url = 'https://www.cityoflaurel.org'
        links_with_dupes = response.css('div#site-main')[0].css('a').xpath('@href').extract()
        links = list(set(links_with_dupes))
        for link in links:
            print("LINK: " + link + '\n')
            if link.endswith('.pdf'):
                yield Request(url=link, callback=self.save_pdf)
            if "http" not in str(link):
                yield Request(url=base_url + link + '/', callback=self.fourth_pass)
            elif "cityoflaurel" in link:
                yield Request(url=link, callback=self.fourth_pass)
            else:
                yield { "link": link }

    def fourth_pass(self, response):
        base_url = 'https://www.cityoflaurel.org'
        links_with_dupes = response.css('div#site-main').css('a').xpath('@href').extract()
        links = list(set(links_with_dupes))
        for link in links:
            print("LINK: " + link + '\n')
            if link.endswith('.pdf'):
                yield Request(url=link, callback=self.save_pdf)
            if "http" not in str(link):
                yield { "link": base_url + link + '/' }
            else:
                yield { "link": link }


    def save_pdf(self, response):
        path = response.url.split('/')[-1]
        with open('PDFs/' + path, 'wb') as f:
            f.write(response.body)
            f.close()
