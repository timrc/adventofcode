from common import run, read_lines

# p=<-717,-4557,2578>, v=<153,21,30>, a=<-8,8,-7>
def p1():
    particles = []
    for line in read_lines(20):
        data = line.split(', ')
        p, p_data = data[0].split('=')
        p_data = [int(x) for x in p_data[1:][:-1].split(',')]
        v, v_data = data[1].split('=')
        v_data = [int(x) for x in v_data[1:][:-1].split(',')]
        a, a_data = data[2].split('=')
        a_data = [int(x) for x in a_data[1:][:-1].split(',')]
        particles.append({
            'p': p_data,
            'v': v_data,
            'a': a_data,
        })

    for x in xrange(10**4):
        if x % 1000 == 0:
            print x
        for idx in xrange(len(particles)):
            particle = particles[idx]
            particle['v'][0] += particle['a'][0]
            particle['v'][1] += particle['a'][1]
            particle['v'][2] += particle['a'][2]
            particle['p'][0] += particle['v'][0]
            particle['p'][1] += particle['v'][1]
            particle['p'][2] += particle['v'][2]

    closest_idx = 0
    closest_distance = 10**50
    for idx in xrange(len(particles)):
        particle = particles[idx]
        distance = abs(particle['p'][0]) + abs(particle['p'][1]) + abs(particle['p'][2])
        if distance < closest_distance:
            closest_idx = idx
            closest_distance = distance

    print closest_idx, closest_distance


def p2():
    particles = []
    for line in read_lines(20):
        data = line.split(', ')
        p, p_data = data[0].split('=')
        p_data = [int(x) for x in p_data[1:][:-1].split(',')]
        v, v_data = data[1].split('=')
        v_data = [int(x) for x in v_data[1:][:-1].split(',')]
        a, a_data = data[2].split('=')
        a_data = [int(x) for x in a_data[1:][:-1].split(',')]
        particles.append({
            'p': p_data,
            'v': v_data,
            'a': a_data,
        })

    for x in xrange(10**4):
        if x % 1000 == 0:
            print x
        collide_zone = {}
        for idx in xrange(len(particles)):
            particle = particles[idx]
            # Increase the X velocity by the X acceleration.
            # Increase the Y velocity by the Y acceleration.
            # Increase the Z velocity by the Z acceleration.
            # Increase the X position by the X velocity.
            # Increase the Y position by the Y velocity.
            # Increase the Z position by the Z velocity.
            particle['v'][0] += particle['a'][0]
            particle['v'][1] += particle['a'][1]
            particle['v'][2] += particle['a'][2]
            particle['p'][0] += particle['v'][0]
            particle['p'][1] += particle['v'][1]
            particle['p'][2] += particle['v'][2]
            key = '%d:%d:%d' % (particle['p'][0], particle['p'][1], particle['p'][2])
            if not collide_zone.get(key):
                collide_zone[key] = []
            collide_zone[key].append(idx)
        to_delete = []
        for k,v in collide_zone.items():
            if len(v) > 1:
                for idx in v:
                    to_delete.append(idx)
        new_particles = [particles[idx] for idx in xrange(len(particles)) if idx not in to_delete]
        particles = new_particles

    print len(particles)

if __name__ == '__main__':
    run(p1, p2)