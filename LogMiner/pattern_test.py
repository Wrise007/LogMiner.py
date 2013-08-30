from pattern_generator import get_substrate 

def hash(list):
	str = ''
	for item in list:
		str = str + '_' + item
	return str

fin = open('iikonet_thread.log', 'r')

string = 'Bonus in order [{clientCardNumber: null, clientPaymentsLimit: null, closeInfo: null, priceCategory: null, defaultPriceCategory: null, discounts: {items: null, disabledDiscounts: [], fixedAppliedDiscounts: []}, items: [{choiceBindingEntries: [], fixedSimpleModifiers: [{maximumAmount: 1, minimumAmount: 0, modifier: f8d113fa-6828-454d-9005-5f662a6719e4}], fixedGroupModifiers: [], fixedContainers: [], selectedContainerIndex: -1, flyerDiscount: null, printed: true, rateSchedule: null, rateScheduleEntries: [], timePayServiceTimeLimit: null, timePayServiceCost: 0, serveGroupNumber: 1, orderRank: 0, cookingStartTime: 06.07.2013 11:42:34, cookingFinishTime: 06.07.2013 11:42:34, printTime: 06.07.2013 11:42:34, deliverTime: 06.07.2013 11:42:34, delivered: true, course: 1, guest: 909837d4-e089-4f61-b88a-c681a78960a7, comment: null, amount: 1, dish: c6334e0c-8b87-95b4-0133-8cf7f94a0f40, fixedPrice: 9100, delMethod: null, copiedFromItemId: 00000000-0000-0000-0000-000000000000, itemSaleEventId: ae2f5042-5435-4a3f-9e7f-fb45dc564081, category: null, kitchen: 300f0c63-ab80-4ab0-b167-14ec9a0bb22b, deleted: false, id: 7c37bfe2-1ea7-47c4-8d64-6b82ae6edcec}, {choiceBindingEntries: [], fixedSimpleModifiers: [{maximumAmount: 1, minimumAmount: 0, modifier: f8d113fa-6828-454d-9005-5f662a6719e4}], fixedGroupModifiers: [], fixedContainers: [], selectedContainerIndex: -1, flyerDiscount: null, printed: true, rateSchedule: null, rateScheduleEntries: [], timePayServiceTimeLimit: null, timePayServiceCost: 0, serveGroupNumber: 1, orderRank: 1, cookingStartTime: 06.07.2013 11:42:34, cookingFinishTime: 06.07.2013 11:42:34, printTime: 06.07.2013 11:42:34, deliverTime: 06.07.2013 11:42:34, delivered: true, course: 1, guest: 909837d4-e089-4f61-b88a-c681a78960a7, comment: null, amount: 1, dish: c6334e0c-8b87-95b4-0133-8cf7f94a0f41, fixedPrice: 9100, delMethod: null, copiedFromItemId: 00000000-0000-0000-0000-000000000000, itemSaleEventId: cc3ec93e-2766-4e36-9e56-1ba753cff5c1, category: null, kitchen: 300f0c63-ab80-4ab0-b167-14ec9a0bb22b, deleted: false, id: 78eca548-d547-446b-b71b-8862a57a5c41}], bonusItems: [], printerCounters: {300f0c63-ab80-4ab0-b167-14ec9a0bb22b=1}, number: 13497, fiscalChequeNumber: null, openTime: 06.07.2013 11:41:03, paymentItems: [], preliminaryPaymentItems: [], prePaymentItems: {}, guests: [{name: Į񲼠1, firstOrderNumber: 13497, penultimateOrderTableNumber: null, previousOrderTableNumber: null, place: 0, orderRank: 0, id: 909837d4-e089-4f61-b88a-c681a78960a7}], positionInWaiterOrders: 0, prechequeTime: 06.07.2013 11:42:34, restaurantSection: 300f0c63-ab80-4ab0-b167-14ec9a0bb22b, status: BILL, tables: [{num: 1, name: , places: [], placesNum: 0, isTimePayTable: true, isPetrolTable: false, defaultProduct: null, lastChangedTerminalId: 00000000-0000-0000-0000-000000000000, syncRevision: 0, deleted: false, lastModifiedHash: 0, revision: 270205, lastModifyNode: null, id: 5103669d-6609-4e40-b42c-7c505d09440f}], waiter: 3da94bc8-9055-4661-95ee-efe5b32279f5, sessionId: 00000000-0000-0000-0000-000000000000, storned: false, isCopyOfStorned: false, sourceOrderId: null, divisions: 1, initialGuestsAmount: 1, newGuestNumber: 1, isEditableOrder: true, reserveId: 00000000-0000-0000-0000-000000000000, billInProgress: false, isPaymentFailedOnCashRegister: false, isShutdownOnClosing: false, wasPrepayed: false, deletedNewItemsAmount: 0, deletedNewItemsSum: 0, nextServeGroupNumber: 4, lastChangedTerminalId: 81e51ea2-d1db-04f9-0133-8db548f60103, syncRevision: 291995, localId: -1, created: 06.07.2013 11:41:03, modified: 06.07.2013 11:42:34, deleted: false, lastModifiedHash: null, revision: 0, lastModifyNode: null, id: 7a8a5e4a-7170-4e59-a9ed-999fc27b145e}]'
result = get_substrate(string)

input()

list = []
dict = {}
while True:
	line = fin.readline()
	if line == '':
		break
	pattern = get_substrate(line)
	if hash(pattern['separator']) in list:
		dict[hash(pattern['separator'])].append(line)
	else:
		list.append(hash(pattern['separator']))
		dict[hash(pattern['separator'])] = [line]
print(len(list))
#for item in list:
#	print (item)
for i in range(0, len(list)):
	print('===Pattern '+ list[i])
	str_list = []
	for item in dict[list[i]]:
		if item not in str_list:
			str_list.append(item)
		
	for item in str_list:
		print (item)

		
#string = 'Create and open channel: 1 Call: 1 Close: 0 Abort: 0 Use POS server [True], settings changed [False] Use POS server [True], address []'