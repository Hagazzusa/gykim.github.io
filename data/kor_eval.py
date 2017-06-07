import sys

answer = [
    [5126],
    [3325, 3330],
    [728, 726],
    [1001, 1196, 2025],
    [3422],
    [2130, 2131, 2132],
    [407],
    [4587, 4588],
    [3911],
    [3891],
    [4564],
    [3885],
    [3950, 1570, 71],
    [5029],
    [1910, 1911, 1883, 1884, 1885],
    [4304, 4305],
    [836, 3952],
    [4688],
    [4127],
    [2838, 4743, 5051, 2802]
]
            
def calc(pred, ans, top=20):
    all_ans = 0
    for qn in ans:
        for temp in qn:
            all_ans += 1
    tp = 0.
    fp = 0.
    fn = 0.
    tn = 0.
    
    all_ap = 0.0
    for idx in range(0, 20):
        cur_tp = 0.0
        temp = 0.
        ap = 0.
        last_temp = 0.
        if top != -1 : pr_temp = pred[idx][:top]
        else : pr_temp = pred[idx]
        for prediction in pr_temp:
            temp += 1
            if prediction in ans[idx]: 
                tp += 1
                cur_tp += 1
                ap += cur_tp/temp
                last_temp = temp
            else: fp += 1
        if last_temp != 0: all_ap += ap/last_temp
        for answer in ans[idx]:
            if answer not in pr_temp: fn += 1
        
    all_ap /= 20
            
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    
    return precision, recall, all_ap
            
if __name__ == '__main__':
    pred = [ [] for i in range(20)]
    with open(sys.argv[1]) as f:
        for line in f:
            temp = line.split()
            pred[int(temp[0])-1].append(int(temp[2]))
    p, r, m = calc(pred, answer, 20)
    _, _, all_m = calc(pred, answer, -1)
    print "top 20 precision : ", p
    print "top 20 recall : ", r
    print "top 20 MAP(Mean Average Precision) : ", m
    print "All MAP : ", all_m
            