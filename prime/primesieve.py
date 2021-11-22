class PrimeSieve:
    """ PrimeSieve, class to implement Sieve of Eratosthenes to pick up prime numbers
    :param sievesize: size of the sieve
    :type sievesize: int

    """
    def __init__(self, sievesize):
        """ Instantiates the sieve """
        self.sieve = [True]*sievesize # Anticipate them being true
        self.populateSieve()
        
    def __str__(self):
        return ', '.join(str(p) for p in self.sieve)
    
    def populateSieve(self):
        """ populateSieve, method to populate the Sieve 
        :param n/a: no parameters so far
        """
        for index, isPotentialPrime in enumerate(self.sieve): 
            prime=index+1
            if prime<4: pass # 1, 2 and 3 are primes,start from 4 onwards
            else:
                #print(prime, isPotentialPrime)
                if isPotentialPrime:
                    if not self.isPrime(2,index+1):
                        self.sieve[index]=False
                        #print(f'setting index={index} to False')
                        #"""
                        for index2 in range(index+prime,len(self.sieve),prime):
                            self.sieve[index2]=False
                            #print(f'setting index2={index2} to False')
                        #"""
    
    def getPrimes(self):
        """ getPrimes, returns the primes in the sieve
        :param n/a: no parameters so far
        :returns: List of primes in the sieve
        """
        primes=[]
        for index, isPotentialPrime in enumerate(self.sieve): 
            prime=index+1
            if isPotentialPrime: primes.append(prime)
            
        return primes
    
    def isPrime(self,start,number):
        """ isPrime, recursive function to decide whether given number is a prime
        :param start: Number to start recursion with. In initial call always 2
        :type start: int
        :param number: Number to be checked for being a prime
        :returns: True or False
        """
        if number <= 1:
            return 
        else:
            if start >= number:
                pass
            else:
                if number == 2: 
                    pass
                elif (number % start) == 0:
                    return False
                else:
                    return self.isPrime(start+1,number)
    
        return True



