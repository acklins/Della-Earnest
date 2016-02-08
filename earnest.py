items = [('zebra',13.00,23),('lion',20.00, 12),('elephant',35.00, 3)];
state_taxes = [('ca',.08),('ny',.06),('mn', 0)]

def verify_pricing( items_p, state_p, price_given ):
    print items
    print state_taxes
    print items_p
    print state_p
    total_price = 0
    # find out which items are in items_p and then detemrine if there is enough then price
    for item_tuple in items_p:
        for item_c in items:
            if item_tuple[0] == item_c[ 0 ]:
                if ( item_tuple[1 ] > item_c[ 2 ] ):
                         print "customer asking for too many", item_tuple[0]
                         return
                item_price = item_tuple[ 1 ] * item_c[ 1 ]
                total_price = total_price + item_price
                print 'item_price for %s is %d' %( item_tuple[ 0], item_price)
    print 'total price before tax is %d' % total_price
    tax  = 0
    for state_item in state_taxes:
        if state_p == state_item[ 0 ]:
            tax = state_item[1]
            print 'tax for state %s is %f' % (state_item[ 0 ], state_item[ 1 ] )
            break
    total_tax = total_price * tax
    total_price = total_price + total_tax
    print 'total price after tax is %d' % total_price
    if int(price_given) != int(total_price):
        print 'price given, %d, is incorrect' % price_given
    else:
        print 'price given, %d, is correct' % price_given

if __name__ == "__main__":
    items_to_buy = [('zebra',3),('lion',2)]
    state = 'ca'
    price_given = 80
    verify_pricing( items_to_buy, state, price_given )
    price_given = 85
    verify_pricing( items_to_buy, state, price_given )
    items_to_buy = [('zebra',3),('lion',200)]
    verify_pricing( items_to_buy, state, price_given )
