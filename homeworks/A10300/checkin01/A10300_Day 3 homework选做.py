
#-*- coding: utf-8 -*-
# @author: Baoshi

def talk_with_daddy(is_cheap3, buy_amount3):
  if is_cheap3:
    print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤”。' %(buy_amount3)
  else:
    print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。'

def buybuy():
  good_price = 3 
  reasonable_price = 5
  buy_amount = 2 
  
  who = 'xiao的老妈'
  good_description = "厦门烧仙草"

  is_cheap = False
  cost = 0
  

  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    
    #5-2 4-3 3-4 2-4
    buy_amount = 2 + (reasonable_price - good_price)
    if buy_amount > 4:
      buy_amount = 4
    print '她买了 %d 斤' % (buy_amount)
    cost = buy_amount * good_price
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'

  return is_cheap, buy_amount, cost, good_description

def record_account(good_description, cost):
  if cost > 0:
  print '老妈记在小本子：今天买了%s, 共花了 %d 元' % (good_description, cost)
  else:
  pass

def main():
  #买买买
  is_cheap2, buy_amount2, cost, good_description = buybuy()
  #说说说
  talk_with_daddy(is_cheap2, buy_amount2)  
  #记记记
  record_account(good_description, cost)

if __name__ == '__main__':
  main() 
