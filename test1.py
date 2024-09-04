import copy
class RiskMonitor:
    def __init__(self, people):
        self.ban_date = [0] * len(people)
        self.station = people
        self.risk_status = [(0, 0) for i in range(1000)]
        self.ban_status = [(0, 0) for i in range(len(people))]

    def travel(self, date, people_id, region_id):
        if self.station[people_id] == region_id:
            return 1

        if self.risk_status[region_id][0] == 1:
            return -1

        cur_station = self.station[people_id]
        if self.risk_status[cur_station][0] == 1:
            return -1

        # 所处位置为低风险
        if self.ban_status[people_id][0] == 1:
            if date - self.risk_status[cur_station][1] >= 14:   # 所处位置是否连续处于低风险14天
                self.ban_date[people_id] += 14
                self.ban_status[people_id] = (0, self.risk_status[cur_station][1] + 14)
                self.station[people_id] = region_id
                return 0
            else:
                return -1
        else:
            self.station[people_id] = region_id
            return 0


    def increase_risk(self, date, region_id):
        self.risk_status[region_id] = (1, date)
        for i in range(len(self.station)):
            if self.station[i] == region_id:
                if self.ban_status[i][0] == 1:
                    if date - self.ban_status[i][1] >= 14:
                        self.ban_date[i] += 14
                    else:
                        self.ban_date[i] += (date - self.ban_status[i][1])
                self.ban_status[i] = (1, date)


    def decrease_risk(self, date, region_id):
        self.risk_status[region_id] = (0, date)
        for i in range(len(self.station)):
            if self.station[i] == region_id:
                self.ban_date[i] += (date - self.ban_status[i][1])
                self.ban_status[i] = (1, date)


    def query(self, date):
        res = self.ban_date.copy()
        for i in range(len(self.station)):
            if self.ban_status[i][0] == 1:
                cur_station = self.station[i]
                if self.risk_status[cur_station][0] == 0:
                    if date - self.ban_status[i][1] >= 14:
                        res[i] += 14
                    else:
                        res[i] += (date - self.ban_status[i][1] + 1)
                else:
                    res[i] += (date - self.ban_status[i][1] + 1)
        return res


# a = RiskMonitor([1])
# print(a.increase_risk(4,1), '\n', )
# print(a.decrease_risk(10,1), '\n',)
# print(a.increase_risk(17,1), '\n',)
# print(a.decrease_risk(20,1), '\n',)
# print(a.query(33), '\n',)
# print(a.travel(33,0,2), '\n',)
# print(a.travel(34,0,3), '\n',)
# print(a.query(34), '\n',)
# print(a.increase_risk(40,3), '\n',)
# print(a.query(40))

a = RiskMonitor([1,1])
print(a.travel(2,1,0), '\n', )
print(a.increase_risk(5,1), '\n',)
print(a.query(5), '\n',)
print(a.travel(19,1,1), '\n',)
print(a.decrease_risk(21,1), '\n',)
print(a.query(22), '\n',)
print(a.travel(25,1,1), '\n',)
print(a.travel(35,0,0), '\n',)
print(a.query(37))



