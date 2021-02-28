import matplotlib.pyplot as plt
from functools import reduce

def calc_avg_unemp(unemp):
    
    def helper(x, y):
        y = float(y) if y.strip() else 0

        return float(x) + float(y)
    
    return round(reduce(helper, unemp) / 12, 3)

def get_all_unemp_statistics():
    avg_unemp = []
    i = 0
    with open("unemp.csv", "r") as f:
        for line in f:
            if not i:
                i += 1
                continue

            line = line.strip().split(",")
            avg_unemp.append(calc_avg_unemp(line[1:]))
            
    return avg_unemp

def get_avg_unemp_by_year(year):
    avg_unemp = []
    i = 0
    with open("unemp.csv", "r") as f:
        for line in f:
            if not i:
                i += 1
                continue

            line = line.strip().split(",")
            if line[0] == year:
                avg_unemp.append(calc_avg_unemp(line[1:]))
                break
            
    return avg_unemp


def calc_avg_gdp(unemp):
    
    def helper(x, y):
        y = float(y) if y.strip() else 0

        return float(x) + float(y)
    
    return reduce(helper, unemp) / 12

def get_gdp_statistics(year=None):
    avg_gdp = []
    
    with open("gdp.txt", "r") as f:
        prev_year = statistics = found = 0
        
        
        for line in f:
            line = line.strip().split()
            
            if not year:
                if prev_year == line[0][:4]:
                    statistics += float(line[1])
                else:
                    if statistics:
                        avg_gdp.append(statistics/4)
                    statistics = 0

                prev_year = line[0][:4]
            else:
                if year == line[0][:4]:
                    found += 1
                    statistics += float(line[1])
                else:
                    if found == 4:
                        avg_gdp.append(round(statistics/4, 3))
                        break
            
    return avg_gdp

def plot(gdp, unemp):
    y = list(range(1948, 2010))
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('change in GPD')
    ax1.set_ylabel('years')
    ax1.plot

    color = 'tab:blue'
    ax1.set_xlabel('years')
    ax1.set_ylabel('Change in GDP', color=color)
    ax1.plot(y, gdp, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:red'
    ax2.set_ylabel('Unemployment range', color=color)
    ax2.plot(y, unemp, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    while True:
        try:
            year = int(input("Type a year: "))
        except:
            print("Type correct year")
            continue
        
        if year < 1948 or year > 2008:
            print("Year should be between 1948 and 2008")
            continue

        break
    
    annual_gdp_statistic = get_gdp_statistics(str(year))
    annual_unemp_statistic = get_avg_unemp_by_year(str(year))
    print(f"For {year}, average GDP: {annual_gdp_statistic} and average unemployment: {annual_unemp_statistic}")

    gdp = get_gdp_statistics()
    unemp = get_all_unemp_statistics()

    plot(gdp, unemp)


