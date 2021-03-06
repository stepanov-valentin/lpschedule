# -*- coding: utf-8 -*-
from grab.spider import Spider
from schedule.models import Time


class TimeParser(Spider):
    BASE = 'http://lp.edu.ua/poyasnennya-do-rozkladu'
    initial_urls = [BASE]

    def prepare(self):
        super(TimeParser, self).prepare()

    def shutdown(self):
        super(TimeParser, self).shutdown()

    @classmethod
    def task_initial(self, grab, task):
        for tr in grab.doc.select('//table[@class="timetable"]/tr')[1:]:
            for key, td in enumerate(tr.select('./td')):
                if key == 0:
                    time = Time.get_by_number(td.text())
                    if time:
                        pass
                    else:
                        time = Time(time_number=td.text().strip())
                if key == 1:
                    tabletime = td.text().split(u'−')
                    time.time_start = tabletime[0].strip()
                    time.time_end = tabletime[1].strip()
                    self.save_time(time)

    @classmethod
    def save_time(self, time):
        Time.add(time)
