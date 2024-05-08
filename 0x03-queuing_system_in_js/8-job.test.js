import createPushNotificationsJobs from './8-job.js';
import { createQueue } from 'kue';
import { expect } from 'chai';
import { describe, it, before, after, afterEach } from 'mocha';

const queue = createQueue();

describe('Test createPushNotificatinsJobs function', () => {
  before( () => {
    queue.testMode.enter();
  });

  afterEach( () => {
    queue.testMode.clear();
  });

  after( () => {
    queue.testMode.exit();
  });

  it('Error message displyed if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('job', queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('Test whether jobs are created', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is Test message 1'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is Test message 2'
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
  });
});
