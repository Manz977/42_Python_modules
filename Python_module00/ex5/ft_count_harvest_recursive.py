def ft_count_harvest_recursive(current_day, final_day):
    if current_day > final_day:
      print("Harvest Time")
      return ;
    
    print("Day", current_day)
    
    ft_count_harvest_recursive(current_day + 1, final_day)


days = int(input("Days until harvest: "))

ft_count_harvest_recursive(1, days)