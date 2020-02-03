#####################################################
# Homework 1 - due 02/04/2020 at noon.
# Professor's name: Dr. Tarau
# Student's name: Svetlana Galuzinschii
#####################################################


def ReadInput() :
    while True:
        try:
            n = int(input("Please enter the size of the set made of integers between 0 and the desired set size-1 for which this application will compute the subsets of:\n"))
            if n<=0:
               print(" Enter a positive integer, please.")
            else:
               break
        except ValueError:
            print(" Enter a positive integer, please.")


    for t in GenerateAllSubsets(n):
        print(t)
    print()
    print ("If you wish to interact with this application when it is running in the interactive mode, \n you can call the function that returns the generator of the subsets \n by executing 'GenerateAllSubsets(n)', where n is the size of the original set.\n")
    print ("An example call would be GenerateAllSubsets(3) to return the generator of subsets of {0,1,2} or list(GenerateAllSubsets(3)) to list all of the subsets on the screen.")

def GenerateAllSubsets(n) :
  print ("Here are all the possible subsets of the set of size",n,"of integers between 0 and",n-1)
  for i in range(2**n) :
    # 'hello'.zfill(8) padds the string with zeros to produce a string of length n, in this example the result would be '000hello'
    # bin(i) returns the binary encoding of the decimal value i
    l=list(str(bin(i))[2:].zfill(n))

    if i>0:
      yield set(DecodeBinaryList(l))
    else:
      yield {}

def DecodeBinaryList(Xs) :
  k=0
  for j in Xs:
    if j == '1':
      yield k
    k=k+1



if __name__ == "__main__" :
  ReadInput()