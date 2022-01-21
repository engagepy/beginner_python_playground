hotel_rates = [3500, 4500, 9000, 20000, 45000]
durations = [3 , 5 , 6, 7, 8]
extra_kids = [1,2,3]
extra_adult = 1

scuba = 4000
kayak_day = 2500
courseow = 33000
courseaow = 29000
candlelightdindin = 10000
transfers2island = 5500
transfers3island = 7500
comm = 15
tax = .05 


package_options = {}
package_no_tax = {}

package_activity_1pax_tax_2islandtrans = {}
package_activity_1pax_pre_tax_2islandtrans = {}

package_activity_2pax_pre_tax_2islandtrans = {}
package_activity_2pax_tax_2islandtrans ={}

package_activity_1pax_tax_3islandtrans = {}
package_activity_1pax_pre_tax_3islandtrans = {}

package_courseow_1pax_pre_tax_2islandtrans = {}
package_courseow_1pax_tax_2islandtrans = {}


package_courseaow_1pax_tax_2islandtrans = {}


extra_pax = {}

class calc:

	def base_room():
		for i in durations:

			#rooms only

			pre_tax = [(x*i) for x in hotel_rates]
			package_no_tax[i] = pre_tax

			with_tax = [pre_tax + (pre_tax * tax) for pre_tax in pre_tax]
			package_options[i] =  with_tax

			#2island + rooms + scuba + kayak for 1pax

			acitiv1_2island = [pre_tax + (scuba * 1) + (kayak_day * 1) + (transfers2island * 1)for pre_tax in pre_tax]
			package_activity_1pax_pre_tax_2islandtrans[i] = acitiv1_2island

			activ1_2island_tax = [acitiv1_2island + (acitiv1_2island * tax) for acitiv1_2island in acitiv1_2island]
			package_activity_1pax_tax_2islandtrans[i] = activ1_2island_tax

			#2island + rooms + scuba + kayak for 2pax

			acitivpax2_island2 = [pre_tax + (scuba * 2) + (kayak_day * 2) + (transfers2island * 2)for pre_tax in pre_tax]
			package_activity_2pax_pre_tax_2islandtrans[i] = acitivpax2_island2

			activpax2_island2_tax = [acitivpax2_island2 + (acitivpax2_island2 * tax) for acitivpax2_island2 in acitivpax2_island2]
			package_activity_2pax_tax_2islandtrans[i] = activpax2_island2_tax

			#3island + rooms + scuba + kaya for 1pax

			acitiv1_3island = [pre_tax + (scuba * 1) + (kayak_day * 1)  + (transfers3island * 1) for pre_tax in pre_tax]
			package_activity_1pax_pre_tax_3islandtrans[i] = acitiv1_3island
			
			activ1_3island_tax = [acitiv1_3island + (acitiv1_3island * tax) for acitiv1_3island in acitiv1_3island]
			package_activity_1pax_tax_3islandtrans[i] = activ1_3island_tax

			#2island + rooms + OW Course for 1pax			

			pax1_course_2island_pre_tax = [pre_tax + courseow + (transfers2island * 1) for pre_tax in pre_tax]
			package_courseow_1pax_pre_tax_2islandtrans[i] = pax1_course_2island_pre_tax

			pax1_course_2island_tax = [pax1_course_2island_pre_tax + (pax1_course_2island_pre_tax * tax) for pax1_course_2island_pre_tax in pax1_course_2island_pre_tax]
			package_courseow_1pax_tax_2islandtrans[i] = pax1_course_2island_tax


			
x = calc.base_room()

print(" ")

for i in durations:
	print(f"Following Calculations Represent Prices Calculated for {i} Nights")

print(" ")

for i in hotel_rates:
	print(f"Hotel Rates Calculated for {i} Categories")

print(" ")

print("VARIATIONS: BACKPACKER, BUDGET, VIBEY, LUXURY, ULTRA-LUXURY")

print(" ")

#for i in package_no_tax:
	#print(f"{i}N  Stay ONLY & NO_TAX" , package_no_tax[i])


for i in package_options:
	print(f"{i}N Stay ONLY & Tax" , package_options[i])

print(" ")


#for i in package_activity_1pax_pre_tax_2islandtrans:
	#print(f"1pax {i}N Kayak + Scuba + Transfer2 & NO_TAX" , package_activity_1pax_pre_tax_2islandtrans[i])


for i in package_activity_1pax_tax_2islandtrans:
	print(f"1pax {i}N Kayak + Scuba + Transfer2 & Tax" , package_activity_1pax_tax_2islandtrans[i])

print(" ")

for i in package_activity_2pax_tax_2islandtrans:
	print(f"2pax {i}N Kayak + Scuba + Transfer2 & Tax" , package_activity_2pax_tax_2islandtrans[i])




#for i in package_activity_1pax_pre_tax_3islandtrans:
	#print(f"1pax {i}N Kayak + Scuba + Transfer3 & NO_TAX" , package_activity_1pax_pre_tax_3islandtrans[i])

print(" ")


for i in package_activity_1pax_tax_3islandtrans:
	print(f"1pax {i}N Kayak + Scuba + Transfer3 & Tax" , package_activity_1pax_tax_3islandtrans[i])



#for i in package_courseow_1pax_pre_tax_2islandtrans:
	#print(f"1pax {i}N Course OW + Transfer2 & NO_TAX" , package_courseow_1pax_pre_tax_2islandtrans[i])

print(" ")


for i in package_courseow_1pax_tax_2islandtrans:
	print(f"1pax {i}N Course OW + Transfer3 & Tax" , package_courseow_1pax_tax_2islandtrans[i])



x =  input("Input to exit")
