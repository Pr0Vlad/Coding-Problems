#told which dominoes fall and where which ones remain standing?
#we can scan left to right and see which dominoes are pushed
class dominoes(object):

    def pushThem(self, dominoes):
        force = 0
        forces = [0] * len(dominoes)
        maxF = len(dominoes)

        for i, d in enumerate(dominoes):
            if d =='R':
                force = maxF
            if d == 'L':
                force = 0
            else:
                force = max(0, force -1)
            forces[i] = force

        for i in range (len(dominoes) - 1, -1, -1):
            d = dominoes[i]
            if d =='L':
                force = maxF
            if d == 'R':
                force = 0
            else:
                force = max(0, force -1)
            forces[i] -= force

        result = ''
        for f in forces:
            if f == 0:
                result += '.'
            elif f > 0:
                result += 'R'
            else:
                result += 'L'
        return result






runner = dominoes()
print(runner.pushThem('..R...L..R.'))